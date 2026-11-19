#
# PySNMP MIB module CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwAnnouncementCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 354))
cwAnnouncementCapability.setRevisions(('2001-10-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwAnnouncementCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwAnnouncementCapability.setLastUpdated('200112260000Z')
if mibBuilder.loadTexts: cwAnnouncementCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwAnnouncementCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwAnnouncementCapability.setDescription('The Agent Capabilities for CISCO-WAN-ANNOUNCEMENT-MIB.')
cwAnnouncementCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 354, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAnnouncementCapabilityV3R00.setDescription('CISCO-WAN-ANNOUNCEMENT-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY", cwAnnouncementCapabilityV3R00=cwAnnouncementCapabilityV3R00, PYSNMP_MODULE_ID=cwAnnouncementCapability, cwAnnouncementCapability=cwAnnouncementCapability)
