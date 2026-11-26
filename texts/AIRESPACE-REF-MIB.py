#
# PySNMP MIB module AIRESPACE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/AIRESPACE-REF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, enterprises, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "enterprises", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
airespace = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179))
airespace.setRevisions(('2005-12-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: airespace.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: airespace.setLastUpdated('200512190000Z')
if mibBuilder.loadTexts: airespace.setOrganization('Airespace, Inc.')
if mibBuilder.loadTexts: airespace.setContactInfo('        Cisco Systems,\n                     Customer Service\n             Postal: 170 West Tasman Drive\n                     San Jose, CA  95134\n                     USA\n                Tel: +1 800 553-NETS\n\n              Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: airespace.setDescription('The Structure of Management Information for the\n             Airespace enterprise.')
mibBuilder.exportSymbols("AIRESPACE-REF-MIB", PYSNMP_MODULE_ID=airespace, airespace=airespace)
