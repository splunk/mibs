#
# PySNMP MIB module CISCOSMB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSMB-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, enterprises, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "enterprises", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2010-10-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cisco.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: cisco.setLastUpdated('201010310000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cisco.setContactInfo('Postal: 170 West Tasman Drive\n\t\tSan Jose , CA 95134-1706\n\t\tUSA\n\n\t\t\n\t\tWebsite:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: cisco.setDescription('The private MIB module definition for CISCOSB private MIB tree.')
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6))
ciscosb = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1))
switch001 = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
rndMib = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
mibBuilder.exportSymbols("CISCOSMB-MIB", ciscosb=ciscosb, PYSNMP_MODULE_ID=cisco, cisco=cisco, switch001=switch001, rndMib=rndMib, otherEnterprises=otherEnterprises)
