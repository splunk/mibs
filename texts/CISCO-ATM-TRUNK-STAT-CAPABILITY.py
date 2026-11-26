#
# PySNMP MIB module CISCO-ATM-TRUNK-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-TRUNK-STAT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
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
ciscoAtmTrunkStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 420))
ciscoAtmTrunkStatCapability.setRevisions(('2005-09-19 00:00', '2004-11-17 00:00', '2004-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setRevisionsDescriptions(('New capabilities for Cisco VISM \n                 Release 3.3.25', 'Updated CANA ID.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setLastUpdated('200509190000Z')
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setDescription('The capabilities description of \n                 CISCO-ATM-TRUNK-STAT-MIB.')
cAtmTrunkStatCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 420, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM33 = cAtmTrunkStatCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM33 = cAtmTrunkStatCapVISM33.setStatus('current')
if mibBuilder.loadTexts: cAtmTrunkStatCapVISM33.setDescription('CISCO-ATM-TRUNK-STAT-MIB capabilities.')
cAtmTrunkStatCapVISM3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 420, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM3325 = cAtmTrunkStatCapVISM3325.setProductRelease('Cisco VISM Release 3.3.25.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM3325 = cAtmTrunkStatCapVISM3325.setStatus('current')
if mibBuilder.loadTexts: cAtmTrunkStatCapVISM3325.setDescription('CISCO-ATM-TRUNK-STAT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ATM-TRUNK-STAT-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmTrunkStatCapability, cAtmTrunkStatCapVISM33=cAtmTrunkStatCapVISM33, ciscoAtmTrunkStatCapability=ciscoAtmTrunkStatCapability, cAtmTrunkStatCapVISM3325=cAtmTrunkStatCapVISM3325)
