#
# PySNMP MIB module CISCO-ENTITY-DIAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DIAG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:43 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntityDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 529))
ciscoEntityDiagCapability.setRevisions(('2010-11-03 00:00', '2009-07-02 00:00', '2009-06-01 00:00', '2008-10-30 00:00', '2008-02-29 00:00', '2007-07-23 00:00', '2007-01-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDiagCapability.setRevisionsDescriptions(('Added capability statement ceDiagCapV12R0250SYPCat6K.', 'Added capability statement ceDiagCapV12R0233SXI2PCat6K.', 'Added capability statement ceDiagCapV12R0252SGPCat4K.', 'Added capability statement ceDiagCapV12R0233SXIPCat6K.', 'Removed variation for ceDiagBootupLevel in ceDiagCapCatOSV08R0601Cat6K.', 'Added capability statement ceDiagCapV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setLastUpdated('201011030000Z')
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setDescription('The capabilities description of CISCO-ENTITY-DIAG-MIB.')
ceDiagCapCatOSV08R0601Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapCatOSV08R0601Cat6K = ceDiagCapCatOSV08R0601Cat6K.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500 series \n                     devices with Supervisor 720 or Supervisor 32 \n                     present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapCatOSV08R0601Cat6K = ceDiagCapCatOSV08R0601Cat6K.setStatus('current')
if mibBuilder.loadTexts: ceDiagCapCatOSV08R0601Cat6K.setDescription('CISCO-ENTITY-DIAG-MIB capabilities.')
ceDiagCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXHPCat6K = ceDiagCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXHPCat6K = ceDiagCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ceDiagCapV12R0233SXHPCat6K.setDescription('CISCO-ENTITY-DIAG-MIB capabilities.')
ceDiagCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXIPCat6K = ceDiagCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXIPCat6K = ceDiagCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ceDiagCapV12R0233SXIPCat6K.setDescription('CISCO-ENTITY-DIAG-MIB capabilities.')
ceDiagCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0252SGPCat4K = ceDiagCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family \n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0252SGPCat4K = ceDiagCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ceDiagCapV12R0252SGPCat4K.setDescription('CISCO-ENTITY-DIAG-MIB capabilities.')
ceDiagCapV12R0233SXI2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXI2PCat6K = ceDiagCapV12R0233SXI2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXI2PCat6K = ceDiagCapV12R0233SXI2PCat6K.setStatus('current')
if mibBuilder.loadTexts: ceDiagCapV12R0233SXI2PCat6K.setDescription('CISCO-ENTITY-DIAG-MIB capabilities.')
ceDiagCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0250SYPCat6K = ceDiagCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0250SYPCat6K = ceDiagCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ceDiagCapV12R0250SYPCat6K.setDescription('CISCO-ENTITY-DIAG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-CAPABILITY", ceDiagCapV12R0233SXIPCat6K=ceDiagCapV12R0233SXIPCat6K, ciscoEntityDiagCapability=ciscoEntityDiagCapability, ceDiagCapV12R0233SXHPCat6K=ceDiagCapV12R0233SXHPCat6K, PYSNMP_MODULE_ID=ciscoEntityDiagCapability, ceDiagCapV12R0252SGPCat4K=ceDiagCapV12R0252SGPCat4K, ceDiagCapV12R0233SXI2PCat6K=ceDiagCapV12R0233SXI2PCat6K, ceDiagCapCatOSV08R0601Cat6K=ceDiagCapCatOSV08R0601Cat6K, ceDiagCapV12R0250SYPCat6K=ceDiagCapV12R0250SYPCat6K)
