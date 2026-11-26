#
# PySNMP MIB module CISCO-WAN-ATM-CONN-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-ATM-CONN-STAT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoWanAtmConnStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoWanAtmConnStatCapability.setRevisions(('2003-04-08 00:00', '2001-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setRevisionsDescriptions(('Added cwacsCapabilityAxsmxgV4R00 for 10 Gig. AXSM \n             Module (AXSM-XG).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setLastUpdated('200304080000Z')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setDescription('The Agent Capabilities for CISCO-WAN-ATM-CONN-STAT-MIB\n                 for different Service Modules in in MGX8850 Series.\n \n                - The cwaConnStatCapabilityAxsmV21R60 is for\n                  ATM Switch Service Module(AXSM).\n                - The cwAtmConnStatCapabilityAxsmeV2R0170 is for\n                  Enhanced AXSM(AXSM-E) module.\n                - The cwAtmConnStatCapabilityPxm1eV2R300 is for\n                  PXM1-E module')
cwaConnStatCapabilityAxsmV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setStatus('current')
if mibBuilder.loadTexts: cwaConnStatCapabilityAxsmV21R60.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities\n                         for ATM Switch Service Module(AXSM).')
cwAtmConnStatCapabilityAxsmeV2R0170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setProductRelease('MGX8850 Release 2.1.70')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnStatCapabilityAxsmeV2R0170.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities\n                         for Enhanced AXSM(AXSM-E) Module.')
cwAtmConnStatCapabilityPxm1eV2R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnStatCapabilityPxm1eV2R300.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities\n                         for PXM1-E Module.')
cwacsCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setStatus('current')
if mibBuilder.loadTexts: cwacsCapabilityAxsmxgV4R00.setDescription('CISCO-WAN-ATM-CONN-STAT-MIB capabilities\n                         for 10 Gig. AXSM Module (AXSM-XG).')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-STAT-CAPABILITY", ciscoWanAtmConnStatCapability=ciscoWanAtmConnStatCapability, cwaConnStatCapabilityAxsmV21R60=cwaConnStatCapabilityAxsmV21R60, PYSNMP_MODULE_ID=ciscoWanAtmConnStatCapability, cwAtmConnStatCapabilityAxsmeV2R0170=cwAtmConnStatCapabilityAxsmeV2R0170, cwAtmConnStatCapabilityPxm1eV2R300=cwAtmConnStatCapabilityPxm1eV2R300, cwacsCapabilityAxsmxgV4R00=cwacsCapabilityAxsmxgV4R00)
