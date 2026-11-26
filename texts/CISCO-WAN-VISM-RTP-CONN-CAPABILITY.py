#
# PySNMP MIB module CISCO-WAN-VISM-RTP-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-RTP-CONN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cwVismRtpConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 337))
cwVismRtpConnCapability.setRevisions(('2001-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismRtpConnCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwVismRtpConnCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setDescription('The Agent Capabilities for CISCO-WAN-RTP-CONN-MIB.')
cwVismRtpConnCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 337, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismRtpConnCapabilityV2R00 = cwVismRtpConnCapabilityV2R00.setProductRelease('VISM Release2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismRtpConnCapabilityV2R00 = cwVismRtpConnCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismRtpConnCapabilityV2R00.setDescription('CISCO-WAN-RTP-CONN-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-RTP-CONN-CAPABILITY", cwVismRtpConnCapabilityV2R00=cwVismRtpConnCapabilityV2R00, cwVismRtpConnCapability=cwVismRtpConnCapability, PYSNMP_MODULE_ID=cwVismRtpConnCapability)
