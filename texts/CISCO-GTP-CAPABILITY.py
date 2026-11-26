#
# PySNMP MIB module CISCO-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GTP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 263))
ciscoGtpCapability.setRevisions(('2003-04-02 09:00', '2002-03-21 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGtpCapability.setRevisionsDescriptions(('Updated for GPRS R4.0 release.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGtpCapability.setLastUpdated('200304020900Z')
if mibBuilder.loadTexts: ciscoGtpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGtpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: ciscoGtpCapability.setDescription('Agent capabilities for CISCO-GTP-MIB')
cGtpCapabilityV12R02Rev08YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setProductRelease('Cisco IOS 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setStatus('current')
if mibBuilder.loadTexts: cGtpCapabilityV12R02Rev08YD.setDescription('CISCO GTP MIB capabilities')
cGtpCapabilityV12R02Rev08YY = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setProductRelease('Cisco IOS 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setStatus('current')
if mibBuilder.loadTexts: cGtpCapabilityV12R02Rev08YY.setDescription('CISCO GTP MIB capabilities for GGSN R3.1.')
cGtpCapabilityV12R02Rev08YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setStatus('current')
if mibBuilder.loadTexts: cGtpCapabilityV12R02Rev08YW.setDescription('CISCO GTP MIB capabilities for GGSN R4.0.')
mibBuilder.exportSymbols("CISCO-GTP-CAPABILITY", ciscoGtpCapability=ciscoGtpCapability, PYSNMP_MODULE_ID=ciscoGtpCapability, cGtpCapabilityV12R02Rev08YW=cGtpCapabilityV12R02Rev08YW, cGtpCapabilityV12R02Rev08YY=cGtpCapabilityV12R02Rev08YY, cGtpCapabilityV12R02Rev08YD=cGtpCapabilityV12R02Rev08YD)
