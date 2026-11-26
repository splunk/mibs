#
# PySNMP MIB module CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwAnnouncementCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 354))
cwAnnouncementCapability.setRevisions(('2001-10-11 00:00',))
if mibBuilder.loadTexts: cwAnnouncementCapability.setLastUpdated('200112260000Z')
if mibBuilder.loadTexts: cwAnnouncementCapability.setOrganization('Cisco Systems, Inc.')
cwAnnouncementCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 354, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY", PYSNMP_MODULE_ID=cwAnnouncementCapability, cwAnnouncementCapabilityV3R00=cwAnnouncementCapabilityV3R00, cwAnnouncementCapability=cwAnnouncementCapability)
